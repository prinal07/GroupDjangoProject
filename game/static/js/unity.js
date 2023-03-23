function checkState() {
    const status = document.getElementById("end-status");
  if (status.innerHTML == "CORRECT") {
      $.ajax({
    type: "POST",
    url: ".",
    data: {
        "give_points": "true"
    },
    success: function(data) {
        console.log("Data Sent Successfully");
    },
    error: function(xhr, status, error) {
        console.log("Error sending data: " + error);
    }
      });

/*    
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'unity' %}");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
      }
    };
    let data = '{"give_points": "true"}';
    xhr.send(data);*/
  }
  else if (status.innerHTML == "INCORRECT") {
    $.ajax({
        type: "POST",
        url: ".",
        data: {
      "give_points": "false"
        },
        success: function(data) {
      console.log("Data sent successfully");
        },
        error: function(xhr, status, error) {
      console.log("Error sending data: " + error);
        }
    });
  /*
  let xhr = new XMLHttpRequest();
    xhr.open("POST", "{% url 'unity' %}");
    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
        console.log(xhr.status);
        console.log(xhr.responseText);
      }
    };

    let data = '{"give_points": "false"}';
    xhr.send(data);*/
  }
  else { }
}

var container = document.querySelector("#unity-container");
var canvas = document.querySelector("#unity-canvas");
var loadingBar = document.querySelector("#unity-loading-bar");
var progressBarFull = document.querySelector("#unity-progress-bar-full");
var fullscreenButton = document.querySelector("#unity-fullscreen-button");
var warningBanner = document.querySelector("#unity-warning");

// Shows a temporary message banner/ribbon for a few seconds, or
// a permanent error message on top of the canvas if type=='error'.
// If type=='warning', a yellow highlight color is used.
// Modify or remove this function to customize the visually presented
// way that non-critical warnings and error messages are presented to the
// user.
function unityShowBanner(msg, type) {
  function updateBannerVisibility() {
    warningBanner.style.display = warningBanner.children.length ? 'block' : 'none';
  }
  var div = document.createElement('div');
  div.innerHTML = msg;
  warningBanner.appendChild(div);
  if (type == 'error') div.style = 'background: red; padding: 10px;';
  else {
    if (type == 'warning') div.style = 'background: yellow; padding: 10px;';
    setTimeout(function () {
      warningBanner.removeChild(div);
      updateBannerVisibility();
    }, 5000);
  }
  updateBannerVisibility();
}

var loaderUrl = "../unity/Build/Build.loader.js";
var config = {
  dataUrl: "../unity/Build/Build.data",
  frameworkUrl: "../unity/Build/Build.framework.js",
  codeUrl: "../unity/Build/Build.wasm",
  streamingAssetsUrl: "StreamingAssets",
  companyName: "DefaultCompany",
  productName: "EcoDetective",
  productVersion: "1.0",
  showBanner: unityShowBanner,
};

// By default Unity keeps WebGL canvas render target size matched with
// the DOM size of the canvas element (scaled by window.devicePixelRatio)
// Set this to false if you want to decouple this synchronization from
// happening inside the engine, and you would instead like to size up
// the canvas DOM size and WebGL render target sizes yourself.
// config.matchWebGLToCanvasSize = false;

if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
  // Mobile device style: fill the whole browser client area with the game canvas:

  /*        var meta = document.createElement('meta');
          meta.name = 'viewport';
          meta.content = 'width=device-width, height=device-height, initial-scale=0.5, user-scalable=yes, shrink-to-fit=yes';
          document.getElementsByTagName('head')[0].appendChild(meta);
          container.className = "unity-mobile";
          canvas.className = "unity-mobile";
  */
  // To lower canvas resolution on mobile devices to gain some
  // performance, uncomment the following line:
  // config.devicePixelRatio = 1;

  //unityShowBanner('WebGL builds are not supported on mobile devices.');

  const canvas = document.querySelector('canvas');

  const aspectRatio = 16 / 9; // Set the aspect ratio to 16:9
  let canvasHeight = window.innerHeight * 0.6; // Set the canvas height based on the window height

  // Adjust the canvas height to maintain the aspect ratio
  let canvasWidth = canvasHeight * aspectRatio;
  if (canvasWidth > window.innerWidth) {
    canvasWidth = window.innerWidth;
    canvasHeight = canvasWidth / aspectRatio;
  }

  // Apply the width and height styles to the canvas element
  canvas.style.width = canvasWidth + 'px';
  canvas.style.height = canvasHeight + 'px';


} else {
  // Desktop style: Render the game canvas in a window that can be maximized to fullscreen:

  canvas.style.width = "960px";
  canvas.style.height = "600px";
}

loadingBar.style.display = "block";

var script = document.createElement("script");
script.setAttribute("src", loaderUrl);
script.setAttribute("type", "text/javascript");
script.onload = () => {
  console.log("SCRIPT load");

  createUnityInstance(canvas, config, (progress) => {
    progressBarFull.style.width = 100 * progress + "%";
  }).then((unityInstance) => {
    loadingBar.style.display = "none";

    console.log("UNITY INSTANCE");

    unityInstance.SendMessage('LogicObject', 'SetSuspectSprites', String("{{spriteCodes}}"));
    unityInstance.SendMessage('LogicObject', 'SetCorrectSuspect', String("{{culprit}}"));
    unityInstance.SendMessage('LogicObject', 'SetClueDescriptions', String("{{clues}}"));
    unityInstance.SendMessage('LogicObject', 'SetSuspectDescriptions', String("{{descriptions}}"));

    fullscreenButton.onclick = () => {
      unityInstance.SetFullscreen(1);
    };
  }).catch((message) => {
    alert(message);
  });
};
document.body.appendChild(script);    
