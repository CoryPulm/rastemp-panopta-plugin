import agent_util
import os

class RPTemperaturePlugin(agent_util.Plugin):
    textkey = "raspi_temp"
    label = "Raspi Temperature"

    @classmethod
    def get_metadata(self, config):
        status = agent_util.SUPPORTED
        msg = None


        # Core Linux
        if not os.path.isfile("/sys/class/thermal/thermal_zone0/temp"):
            msg = "Either not a Raspi or thermal zone file does not exist!"
            status = agent_util.UNSUPPORTED
            return {}

        metadata = {
            "cpu_temp": {
                "label": "CPU Temperature",
                "options": None,
                "status": status,
                "error_message": msg,
                "unit": "C"
            },
            "gpu_temp": {
                "label": "GPU Temperature",
                "options": None,
                "status": status,
                "error_message": msg,
                "unit": "C"
            },
        }

        return metadata

    def check(self, textkey, data, config={}):
        if textkey == 'cpu_temp':
            cpu_temp = 0
            runs = 0
            raw_temp = ''
            while cpu_temp == 0 and runs < 3:
                ret, raw_temp = agent_util.execute_command("cat /sys/class/thermal/thermal_zone0/temp")
                t1 = float(raw_temp) / 1000
                t2 = float(raw_temp) / 100
                cpu_temp = float(t2 % t1)
                runs += 1
                self.log.error("Raw: %s - Measured: %s" % (raw_temp.strip(), cpu_temp))
                if cpu_temp == 0:
                    self.log.warning("CPU temp of '%s' doesn't seem right. Measuring again..." % raw_temp.strip())

            if runs >= 3:
                self.log.error("Invalid CPU temp of '%s'. Retried 3 times and got same result!" % raw_temp.strip())

            return float("%.1f" % cpu_temp)

        if textkey == 'gpu_temp':
            ret, raw_temp = agent_util.execute_command("/opt/vc/bin/vcgencmd measure_temp")
            gpu_temp = raw_temp.replace("temp=", "")
            gpu_temp = gpu_temp.replace("'C", "")
            return float(gpu_temp)

        return 1337
