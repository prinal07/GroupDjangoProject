let qrChecker = false;
const scanner = new Html5QrcodeScanner('reader', {
    // Scanner will be initialized in DOM inside element with id of 'reader'
    qrbox: {
        width: 200,
        height: 200,
    },  // Sets dimensions of scanning box (set relative to reader element width)
    fps: 20, // Frames per second to attempt a scan
});


scanner.render(success, error);
// Starts scanner
const Bins = ['qjdkiivbbunmue625ljyjy04w941jy',
    '3w7wzif7eku0huro54jtmlbt8s0fnm',
    '8xycn8zhxb203qhqw7v2eetrvcscx1',
    'kx6rrxmm29i1w1xtewyk6hqfri57rx',
    'wco52yz8tnu1183lpcohurxdoy90ui',
    '4j2k7xvc2izzteraom2ru2mo3r2sit',
    '12fb5e11lkymrdjrpb6fnhlgtlg2d5',
    'mva7vu8uhg7p1vcg3jt4ueu9vozko5',
    '2btu7id05cxlqzpjusofaihs1gkd4q']

function success(result) {
    //console.log(result);
    for (i = 0; i < Bins.length; i++) {
        if (result.includes(Bins[i])) {
            qrChecker = true;

            document.getElementById('result').innerHTML = `
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
            </style>`
            break;
        }
    }

    if (!qrChecker) {
        document.getElementById('result').innerHTML = `
        <h2>Invalid Qr code!</h2>
        <button onClick="window.location.reload();">Try again</button>`
    }

    // Prints result as a link inside result element

    scanner.clear();
    // Clears scanning instance

    document.getElementById('reader').remove();
    // Removes reader element from DOM since no longer needed
}

function error(err) {
    //console.error(err);
    // Prints any errors to the console
}