frappe.ready(function() {
	const urlParams = new URLSearchParams(window.location.search);
	console.log(urlParams.get('named'));
	// add language picker in navbar
	// append to list 
	li = document.createElement("li")
	li.classList.add('nav-item');
	// add language picker in navbar
	li.innerHTML = "<select id='language-select' class='form-control' style='width: auto;'><option value='en'>English</option><option value='ar'>العربية</option></select>"
	document.querySelector("#navbarSupportedContent").childNodes[3].appendChild(li)
	// change the footer
	document.querySelector(".page-footer").innerHTML = `<div class="left-images">
	<div class="d-flex align-items-end" style="border-top: 3px solid #000">
      <div>
        <img src="/files/3-Logo-L.png" width="100" height="100">
      </div>
      <div style="font-weight: bold; font-size: .8rem;">
        <a href="mailto:info@vim.sa (+ 966) 800-244-0306" style="color: black;">info@vim.sa (+ 966) 800-244-0306</a>
      </div> 
    </div>
  </div>`
  // change the logo in the navbar
  document.querySelector(".navbar-brand").innerHTML = `<img src="/files/Asset 4.png" href="/" alt="Logo" />`

// get the preferred language in this session and set it on the language picker
var preferred_language = frappe.get_cookie("preferred_language")
console.log(preferred_language)
if (preferred_language){
    $('#language-select').val(preferred_language)
}

// whenever the language changes, redirect to its corresponding page in the other language
$('#language-select').on('change', function() {
  frappe.call("frappe.translate.get_preferred_language_cookie", {
    preferred_language: this.value
  }).then(function() {
    var preferred_language = frappe.get_cookie("preferred_language")
    var english_version = $('meta[name=english_version]').prop('content'); // get the link to the english version
    var arabic_version = $('meta[name=arabic_version]').prop('content'); // get the link to the arabic version
    if (preferred_language === "en" && english_version){
        window.location.pathname = english_version
    } else if (preferred_language === "ar" && arabic_version){
        window.location.pathname = arabic_version
    }
  })
});
})
