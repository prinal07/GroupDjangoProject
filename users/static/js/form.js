
var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
	// This function will display the specified tab of the form...
	var x = document.getElementsByClassName("tab");
	x[n].style.display = "block";
	//... and fix the Previous/Next buttons:
	if (n == 0) {
		document.getElementById("prevBtn").style.display = "none";
	} else {
		document.getElementById("prevBtn").style.display = "inline";
	}
	if (n == x.length - 1) {
		document.getElementById("nextBtn").innerHTML = "Submit";
	} else {
		document.getElementById("nextBtn").innerHTML = "Next";
	}
	//... and run a function that will display the correct step indicator:
	fixStepIndicator(n);
}

function nextPrev(n) {
	// This function will figure out which tab to display
	var x = document.getElementsByClassName("tab");
	// Exit the function if any field in the current tab is invalid:
	if (n == 1 && !validateForm()) return false;
	// Hide the current tab:
	x[currentTab].style.display = "none";
	// Increase or decrease the current tab by 1:
	currentTab = currentTab + n;
	// if you have reached the end of the form...
	if (currentTab >= x.length) {
		// ... the form gets submitted:
		document.getElementById("regForm").submit();
		return false;
	}
	// Otherwise, display the correct tab:
	showTab(currentTab);
}

function validateForm() {
	// This function deals with validation of the form fields
	var x,
		y,
		z,
		i,
		j,
		valid = true;
	x = document.getElementsByClassName("tab");
	y = x[currentTab].getElementsByTagName("input");
	z = x[currentTab].getElementsByTagName("select");
	// loops that checks every input field in the current tab:

	//for select fields
	for (j = 0; j < z.length; j++) {
		if (z[j].value == "") {
			//add invalid class to the field
			z[j].className += " invalidSelect";
			// set the current valid status to false
			valid = false;
		}
	}

	// for input fields
	for (i = 0; i < y.length; i++) {
		// If a field is empty...
		if (y[i].value == "") {
			// add an "invalid" class to the field:
			y[i].className += " invalid";
			// and set the current valid status to false
			valid = false;
		}
	}
	// If the valid status is true, mark the step as finished and valid:
	if (valid) {
		document.getElementsByClassName("step")[currentTab].className += " finish";
	}
	return valid; // return the valid status
}

function fixStepIndicator(n) {
	// This function removes the "active" class of all steps...
	var i,
		x = document.getElementsByClassName("step");
	for (i = 0; i < x.length; i++) {
		x[i].className = x[i].className.replace(" active", "");
	}
	//... and adds the "active" class on the current step:
	x[n].className += " active";
}



function emailCheck() {


	email = document.querySelector('#emailInput').value
	address = email.split('@').pop()
	dotCount = email.substring(0, email.indexOf("@")).split(".").length - 1;


  	if (address != "exeter.ac.uk"){
  		toggleWrongEmail(1);
  	} else {
  		toggleWrongEmail(2);
	}

	const departmentTR = document.getElementById('departmentSelect');
	const accomodationTR = document.getElementById('accomodationSelect');

    if (dotCount == 0) {
      	// is a student - show accomodations - use python to pull from group list
  		accomodationTR.style.display = '';
  		departmentTR.style.display = 'none';
    } else if(dotCount == 1) {
      	// is staff - show departments - use python to pull from group list
		  departmentTR.style.display = '';
		accomodationTR.style.display = 'none';
    } else {
    	// invalid email - too many periods
    }

}


function toggleWrongEmail(num) {
	const wrongEmailDiv = document.getElementById('wrongemail');

	if (num == 1){
  		wrongEmailDiv.style.display = 'block';
	} else {
		wrongEmailDiv.style.display = 'none';
	}
  
}

 function passwordCheck(){
	if (password1.length < 8) {
      alert("Password must be at least 8 characters long!");
    }

    if (!/\d/.test(password1)) {
      alert("Password must contain at least one number!");
    }

    if (/^\d+$/.test(password1)) {
      alert("Password must contain at least one non-numeric character!");
    }
 }


 function duplicatePasswords() {
    var password1 = document.getElementById("password").value;
    var password2 = document.getElementById("password2").value;

    if (password1 != password2) {
      alert("Passwords do not match!");
    }

  }
