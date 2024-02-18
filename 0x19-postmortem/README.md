## Postmortem

Issue:

  Duration: The outage occurred on February 16, 2024 (UTC) between 10:00 AM and 12:30 PM.
  Impact: A complete service failure occurred, affecting all users using the platform. About 75% of the user base was affected, rendering critical functions unusable.
  Root Cause: The root cause of the outage was identified as a misconfigured firewall rule blocking incoming traffic to the application servers.

Timeline:

 10:00 (UTC): A problem was detected with automatic trace alerts showing a significant decrease in server response times.
  10:05: Engineers began investigating possible causes, including examining server logs and network settings.
  10:30: The initial assumption indicated a possible overload of the database due to increased traffic. Database queries have been optimized to alleviate potential stress.
  11:00: No service performance improvement detected despite optimization. The survey moved into the network infrastructure.
  11:30: Engineers discovered a misconfigured firewall rule that blocks traffic entering application servers.
  11:45: Incident forwarded to senior network engineers for immediate resolution.
  12:30 PM: Fixed an incorrectly defined firewall rule which restored normal traffic flow to the application servers and fixed the outage.

Cause and workaround:

  Cause: The outage was caused by a misconfigured firewall rule that accidentally blocked incoming traffic to the application servers. This mismatch probably occurred during recent network updates.
  Resolution: The issue was resolved by fixing the firewall rule to allow inbound traffic to the application servers. In addition, a comprehensive network configuration check was performed to identify and correct the corresponding incorrect settings.

Fixes and Preventive Actions:

  Improvements/Ranks:
  Implement stricter change control procedures to prevent mismatches during network updates.
  Improve automatic monitoring systems to provide more detailed information about network traffic and settings.
  Perform regular network configuration checks to proactively detect and correct potential misconfigurations.

Tasks to resolve this issue:

1. Review and modify change control procedures to include rigorous testing and validation steps for online updates.
2. Improve the monitoring system to provide real-time alerts on any significant changes in network configuration.
3. Conduct extensive training for network operations teams to ensure awareness of firewall and network configuration management best practices.
4. Schedule regular network configuration checks to identify and promptly correct misconfigurations.
