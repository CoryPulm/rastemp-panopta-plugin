<h5>This is a plugin for Panopta's on server monitoring agent that reports back to their services to keep track of what your Raspberry Pi's temperatures.</h5>

<h6> You can sign up for Panopta <a href='http://www.panopta.com/'>here</a> and download the monitoring agent <a href='http://answers.panopta.com/how-do-i-install-and-configure-a-panopta-monitoring-agent-v-2/'>here</a></h6>

<strong>Requirements:</strong>
<br />
Panopta agent - Install and make sure to add panopta-agent user to the video group:
`usermod -a -G video panopta-agent`
<br />
Python 2.7
<br />
<strong>Install</strong>
<br />
Just download this and drop it into your plugins folder:
<br />
`/usr/share/panopta-agent/`
<br />
Then run the agent command to rebuild the metadata:
<br />
`python /usr/bin/panopta-agent/panopta_agent.py --rebuild-metadata`

