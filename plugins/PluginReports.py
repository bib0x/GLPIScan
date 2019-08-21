from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginReports:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'reports')
        if version:
            Exploits().verifExploit(info[1], version)
