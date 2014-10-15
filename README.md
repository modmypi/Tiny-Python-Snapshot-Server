Tiny-Python-Snapshot-Server
===========================

<p>The following sample runs a web server on port 8080 and captures images every 5 seconds.</p>
<b>Usage</b>
<ol>
  <li>Save the script as 'snapshot.py' at the root of the /home directory.</li>
  <li>Make 'snapshot.py' executable with 'chmod +x snapshot.py'.</li>
  <li>Run the script from the /home directory: './snapshot.py' or on boot using the '@reboot' cron directive.</li>
  <li>Access the latest snapshot using a web browser like this: "http://localhost:8080/latest.jpg". Replace with the IP address or the domain name of the tiny web server to access the snapshot server remotely.</li>
  <li>'snapshot.py' attempts to load the image capture settings for a file named 'snapshot.txt' if it is present in the '/home' directory. If it does not exist, the script uses default settings as defined in the 'DefaultPictureSettings' variable in the script.</li>
  <li>Ensure that the security settings on the 'snapshot.txt' and 'snapshot.py' files restrict access to the intended user / user group.</li>
</ol>
