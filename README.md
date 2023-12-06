#  Snipe-it Checkout Location&Asset

Why should I use this script？

1. When I was using the Snipe IT system, I found that I could not check out locations and assets in batches. This troubles me.
2. I started to search for some plug-ins on the entire Internet to implement this function. I found a snipe-it-bulkedit-master that can be used, but it needs to be used with Google online forms. Google Sheets can use UrlFetchApp to call the remote interface through scripts, but there are restrictions on calling the local interface directly. This is because Google Apps Script runs on Google servers and does not have direct access to the local network or localhost.
If your local interface is publicly accessible, i.e. accessible via a public IP address or domain name, then you can access it via UrlFetchApp. But if it is a local non-public interface, generally speaking, it cannot be called directly by Google Sheets.
A common solution is to deploy the local interface on a public server and access it via a public address. If your interface requires access to the local network, you may need to set up security measures, such as a VPN or other secure proxy.
Also, make sure your interface is served over HTTPS, as Google Apps Script requires external access over a secure connection. So this is an unsafe behavior.
3. I started using python to create a corresponding plug-in, which I named Snipe-it  Checkout Location&Asset
4. The necessary conditions for using this script are as follows:
    4.1 Obtain Snipe-it API Key
    4.2 Get the data asset ID you want to import in batches through API Get
    4.3 You can get data through Postman
    4.4 Use this link https://data.page/ to convert the data you want into human identifiable data
     4.5 After completion, run the script to import data
