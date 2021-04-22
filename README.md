# Webautomation
## Selenium  
Web automation is the concept of controlling the browser through a code and carrying out specific tasks and processes on any web application. And Selenium WebDriver is a collection of open source APIs which are used to automate the browser. Automation scripts use Selenium commands for emulating user actions on a web page.  

## How does it work?  
When the automation script is executed, the following steps happen:  

~ for each Selenium command, a HTTP request is created and sent to the browser driver   
~ the browser driver uses a HTTP server for getting the HTTP requests  
~ the HTTP server determines the steps needed for implementing the Selenium command  
~ the implementation steps are executed on the browser   
~ the execution status is sent back to the HTTP server  
~ the HTTP server sends the status back to the automation script  

