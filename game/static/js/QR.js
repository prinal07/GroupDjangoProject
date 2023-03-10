/**
 * This variable checks if QR is valid or not
 */
 const qrChecker = false;

 /**
  * Creates a new scanner object inside the element with an ID of "reader".
  * Sets the dimensions of the scanning box relative to the width of the reader element.
  * Sets the number of frames per second to attempt a scan.
  */
 const scanner = new Html5QrcodeScanner('reader', {
     qrbox: {
         width: 200,
         height: 200,
     },
     fps: 20,
 });
 
 /**
  * Renders the scanner on the page and begins scanning.
  */
 scanner.render(success, error);
 
 /**
  * Array of valid QR codes.
  */
 const Bins = ['qjdkiivbbunmue625ljyjy04w941jy',    '3w7wzif7eku0huro54jtmlbt8s0fnm',    '8xycn8zhxb203qhqw7v2eetrvcscx1',    'kx6rrxmm29i1w1xtewyk6hqfri57rx',    'wco52yz8tnu1183lpcohurxdoy90ui',    '4j2k7xvc2izzteraom2ru2mo3r2sit',    '12fb5e11lkymrdjrpb6fnhlgtlg2d5',    'mva7vu8uhg7p1vcg3jt4ueu9vozko5',    '2btu7id05cxlqzpjusofaihs1gkd4q']
 
 /**
  * Runs when the scanner successfully scans a QR code.
  * Loops through the array of valid QR codes and checks if the scanned QR code matches any of them.
  * Displays a message indicating success if the scanned QR code is valid.
  * Displays a message indicating invalid QR code if none of the valid QR codes match the scanned QR code.
  * Clears the scanner instance and removes the reader element from the DOM when finished.
  * @param {string} result - The value of the scanned QR code.
  */
 function success(result) {
     for (i = 0; i < Bins.length; i++) {
         if (result == Bins[i]) {
             document.getElementById('result').innerHTML = `
             <h2>Success!</h2>
             <style> 
         .btn {
             display: inline-block;
             margin-top: 30px;
             padding: 10px 20px;
             font-size: 1.2rem;
             font-weight: bold;
             text-transform: uppercase;
             color: #fff;
             background-color: #333;
             border: none;
             border-radius: 5px;
             cursor: pointer;
             transition: background-color 0.3s ease;
             position: absolute;
             bottom: 550px;
             left: 60%;
             transform: translateX(-50%);
         }
     </style>
         `
         } else if (i == 8) {
             document.getElementById('result').innerHTML = `
             <h2>Invalid Qr code!</h2>
             <button onClick="window.location.reload();">Try again</button>
             `
         }
     }
     scanner.clear();
     document.getElementById('reader').remove();
 }
 
 /**
  * Runs when there is an error with the scanner.
  * Prints any errors to the console.
  * @param {object} err - The error object returned by the scanner.
  */
 function error(err) {
     console.error(err);
 }
 