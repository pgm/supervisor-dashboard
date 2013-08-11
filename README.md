supervisor-dashboard
====================

A lightweight dashboard which aggregates status from supervisord onto a single page.

This dashboard depends on bottle.py ( http://bottlepy.org/ )

This dashboard assumes that there is one supervisor file per host running supervisor, and the 
filename (excluding suffix) is the name of the host running supervisor.   To launch, provide 
the paths to the supervisor configs.  For example:

python dashboard.py ~/supervisor_configs/*.ini
