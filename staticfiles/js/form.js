
var currentTab = 0; // First/Current tab is set to 0
showTab(currentTab); // Display the current tab

// set accommodation default select element to disabled
const accomSelect = document.querySelector('#accomSelect');
const noneOption1 = accomSelect.querySelector('option[value="none"]');
noneOption1.disabled = true;


/**
 * Displays specified tab of the form
 * @param {int} n the tab to be displayed
 */
function showTab(n) {
	var x = document.getElementsByClassName("tab");
	x[n].style.display = "block";

	// hide previous button when on the first tab
	if (n == 0) {
		document.getElementById("prevBtn").style.display = "none"; 
	} else {
		document.getElementById("prevBtn").style.display = "inline";
	}

	// Replace next button with submit button when on the last tab
	if (n == x.length - 1) {
		document.getElementById("nextBtn").innerHTML = "Submit";
	} else {
		document.getElementById("nextBtn").innerHTML = "Next";
	}
	
	fixStepIndicator(n); // display correct step indicator
}

/**
 * Switches tabs when next or previous button is clicked
 * @param {int} n 1 is for next, -1 is for previous 
 */
function nextPrev(n) {
	// This function will figure out which tab to display
	var x = document.getElementsByClassName("tab");

	if (n == 1 && !validateForm()) return false; // if any fields are invalid, dont switch tabs

	x[currentTab].style.display = "none"; // Hide the current tab:
	
	currentTab += n; // Increase or decrease the current tab by 1:

	if (currentTab >= x.length) { // Final tab
		document.getElementById("regForm").submit(); // form submission
		return false;
	}
	showTab(currentTab); // Otherwise, display the correct tab:
}

/**
 * Checks the value and validity of the form fields
 * @returns True if current tab fields are valid, otherwise false
 */
function validateForm() {
	x = document.getElementsByClassName("tab");
	y = x[currentTab].getElementsByTagName("input");
	z = x[currentTab].getElementsByTagName("select");
	selectValid = true;
	inputValid = true;
	emailValid = true;
	password1Valid = true;
	password2Valid = true;
	
	// for select fields
	for (j = 0; j < z.length; j++) {
		if (z[j].value == "none") {
			z[j].className += " invalidSelect"; //add invalid class to the field
			selectValid = false;
		}
	}

	// for input fields
	for (i = 0; i < y.length; i++) {
		// If a field is empty
		if (y[i].value == "") {	
			y[i].className += " invalid"; // add an "invalid" class to the field
			inputValid = false;
		}
	}

	// if first tab -> validate email
	if (currentTab == 0) {
		emailValid = emailCheck()
	}

	// if final tab -> validate passwords
	if (currentTab == x.length-1) {
		password1Valid = passwordCheck()
		password2Valid = duplicatePasswords()
	}

	if (selectValid && inputValid && emailValid && password1Valid && password2Valid) {
		document.getElementsByClassName("step")[currentTab].className += " finish";
		return true;
	}
	return false;
	
	// If the valid status is true -> add finished class to step
	// if (valid) {
	// 	document.getElementsByClassName("step")[currentTab].className += " finish";
	// }
	// return valid; // return the valid status
	
	// TODO: CHECK EMAIL
}

/**
 * Removes active class from all steps, then adds it to the current step
 * @param {int} n current tab
 */
function fixStepIndicator(n) {
	x = document.getElementsByClassName("step");

	for (i = 0; i < x.length; i++) {
		x[i].className = x[i].className.replace(" active", "");
	}

	x[n].className += " active";
}


/**
 * Checks that the email is a valid email for the university of exeter 
 * by checking that the text after the '@' is == 'exeter.ac.uk'
 * @returns true if email is valid, false if not
 */
function emailCheck() {
	emailValidity = false;
	email = document.querySelector('#emailInput').value;
	address = email.split('@').pop();

	if (address != "exeter.ac.uk") {
		toggleWrongEmail(1);
		emailValidity = false;	
  	} else {
		toggleWrongEmail(2);
		emailValidity = true;	
	}

	return emailValidity;
}

/**
 * Displays a message when there's an invalid email
 * @param {int} num 1 is show wrong email message, anything else hides it
 */
function toggleWrongEmail(num) {
	const wrongEmailDiv = document.getElementById('wrongEmail');
	const wrongEmailLi = document.getElementById('wrongEmailLi');
	const emailInput = document.getElementById('emailInput');

	if (num == 1) { // invalid email -> show invalid message
		wrongEmailDiv.style.display = 'block';
		wrongEmailLi.innerHTML = "Must end in @exeter.ac.uk"
		emailInput.className += " invalid"
	} else if (num == 2) { // valid email -> hide invalid message
		wrongEmailDiv.style.display = 'none';
		emailInput.className = ""
	}
}


var password1 = document.getElementById("password");
var password2 = document.getElementById("password2");
var passReq1 = document.getElementById("passReq1");
var passReq2 = document.getElementById("passReq2");
var passReq3 = document.getElementById("passReq3");
	
/**
 * Checks that the password is valid
 * @returns true if password passes all checks, otherwise false
 */
function passwordCheck() {
	passCheck = password1.value

	// Check password is over 8 characters
	minimumLength = false
	if (passCheck.length > 8) {
		passReq1.style.display = "none"
		minimumLength = true;
	} else {
		console.log("password too short")
		passReq1.style.display = "list-item"
		minimumLength = false;
	}

	// Check for at least one numeric character
	hasNumeric = false;
	if (!/\d/.test(passCheck)) {
		console.log("does not have numeric character")
		passReq2.style.display = "list-item"
		hasNumeric = false;
	} else {
		passReq2.style.display = "none"
		hasNumeric = true;
	}

	// Check for at least one non-numeric character
	hasNonNumeric = false;
	if (/^\d+$/.test(passCheck) || passCheck == '') { 
		hasNonNumeric = false;	
		console.log("does not have non-numeric character")
		passReq3.style.display = "list-item"
	} else {
		passReq3.style.display = "none"
		hasNonNumeric = true;
	}

	// Check if password passes all tests
	if (hasNonNumeric && hasNumeric && minimumLength) {
		password1.className = ""
		return true;
	} else {
		password1.className = "invalid"
		return false;
	}
}

/** 
 * Checks that both passwords match
 * @returns true if they match, false if they dont
 */
function duplicatePasswords() {
	var passDuplicate = document.getElementById("passDuplicate");

	if (password1.value == password2.value) {
		passDuplicate.style.display = "none"
		password2.className = ""
		return true
	} else {
		passDuplicate.style.display = "list-item"
		password2.className = "invalid"
		return false
	}

}
