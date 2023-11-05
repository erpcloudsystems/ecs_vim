/**
 * Form with multiple steps
 * Description:
 * Author: Chris Shabani Muswamba (smstudio)
 */
frappe.dom.freeze()
frappe.call({
    method: "ecs_vim.www.user-details.index.checked_finished_details",
    callback: function(r){
        if (r.message){

            window.location.href = frappe.utils.sanitise_redirect(r.message);
        }else{
            frappe.dom.unfreeze()
        }
    },
    freeze: true,
    freeze_message: "Verifying...",
});

//Get sections (steps)
var step1 = document.getElementById("step-1");
var step2 = document.getElementById("step-2");
var prev = document.getElementById('prev');
var step3 = document.getElementById("step-3");
// Default style step display: block
step1.style.display = "block";
// step2 display:  none 
// Preview back display none
step2.style.display = "none";
// Step 3 display: none 
step3.style.display = "none";

//Inputs 
var fname = document.getElementById("form-fname");
var lname = document.getElementById("form-lname");
var email = document.getElementById("form-email");
var phone_no = document.getElementById("form-phone_no");
var batchSelect = document.getElementById("batchSelect");
var formAddress = document.getElementById("form-address");
var gender = document.getElementById("genderSelect");
var datePicker = document.getElementById("datePicker");
var phone = document.getElementById('form-phone');
// step two inputs

//Inputs 2
var fname2 = document.getElementById("form-fname2");
var lname2 = document.getElementById("form-lname2");
var email2 = document.getElementById("form-email2");
var phone_no2 = document.getElementById("form-phone_no2");
var batchSelectTwo = document.getElementById("batchTrackTwo");
var formAddress2 = document.getElementById("form-address2");
var genderSelectTwo2 = document.getElementById("genderSelectTwo");
var datePicker2 = document.getElementById("datePicker2");
var phone2 = document.getElementById('form-phone2');

//Inputs 3
var fname3 = document.getElementById("form-fname3");
var favoriteCharacter = document.getElementById("favorite-character");
var datePicker3 = document.getElementById("datePicker3");
var genderSelectid = document.getElementById("genderSelectthree");
var school = document.getElementById("school");
var favoriteColor = document.getElementById("favorite-color");

// Define form and prevent default submittion 
let form = document.getElementById("stepper-form").addEventListener("click", (e) => {
    // Prevent default submittion
     e.preventDefault();
    //On click we call functions next and prev 
    //  Next function (next button)
     next;
    //Preview or back (button)
     prev;
});

//Progress bar (The progress by default 25%, so when section is completed += 25% width and so on.)
var progressBar = document.getElementById("prgBar");
// Default color is orange (on 50% width color will change, 75% and 99 %)
progressBar.style.backgroundColor = "orange";

//Next(Button) step function. (When this function is excute, we change the style for current sectino to none, the next section to be block) 
var next = document.getElementById("next");
function closePopup(){
    popup.classList.remove('open-popup')
    }
//On click we change the style 
let renderStepTwo = ()=>{
    step2.style.display = "block";
    //Set progress bar width
    progressBar.style.width = "25%";
    //Set progress bar color to blue
    progressBar.style.backgroundColor = "rgb(11, 48, 148)";

    //Change the innerHTML text = 50%
    progressBar.innerHTML = "25%";

    //And set style to none
    step1.style.display = "none";
    //And style to none
    step3.style.display = "none";
}
let renderStepthree = ()=> {
// Add style display none for step 2 (section)
// Add style display none for step 2 (section)
step2.style.display = "none";
// Add style display: none 
step1.style.display = "none";
//And add style display: block
step3.style.display = "block";
//Set progress bar width
progressBar.style.width = "75%";
//Set progress bar color 
progressBar.style.backgroundColor = "lightgreen";
// Set progress bar innerHTML text to = 98%
progressBar.innerHTML = "75%";
let innerDivv = document.getElementById('other-color')
innerDivv.style.display = "none"

const select = document.getElementById('favorite-color');

select.addEventListener('change', function handleChange(event) {
  if (event.target.value == "Other") {
    let innerDivv = document.getElementById('other-color')
    // Now create and append to iDiv
    innerDivv.style.display = "flex"
  } else {
    let innerDivv = document.getElementById('other-color')

    if (innerDivv !== null) {
        innerDivv.style.display = "none"
    }
    
  }

});

}
let appendToUL = (value)=> {
            let ul = document.createElement('ul');
            ul.className = "list-group list-group-flush";    
            // Create a list 
            let item1 = document.createElement('li');

            // Add class 
            item1.className = "list-group-item";

            //Append text 
            item1.innerHTML = `${value} غير مفعل`;
            
            // Append
            ul.append(item1);
            let item2 = document.createElement('li');

            // Add class 
            item2.className = "list-group-item";

            //Append text 
            item2.innerHTML = `<p>برجاء تفعيل الحساب أولا للحصول على كوبون الخصم</p>
            <br>
            <a href="/send-email"> Verifiy Now</a> 
            `;
            ul.append(item2);

            document.getElementById("cardForm").append(ul);
}
const getcheckEmailVerification = async () => {
    frappe.call({
        method: "ecs_vim.www.user-details.index.verify_account",
        callback: function(r) {
            if (r) {
                if (r["message"]["email_verified"] && r["message"]["mobile_no_verified"]) {
                    console.log(r)  

                //Set progress bar width
                progressBar.style.width = "100%";
                //And change the progress bar color
                progressBar.style.backgroundColor = "green";
                // Change the progress innnerHTML = 100%
                progressBar.innerHTML = "100%";
                //Change the innerHTML text = submit
                next.innerHTML = "تسجيل";
            } 
            
            if (!r["message"]["email_verified"]) {
                appendToUL(`Email ${r["message"]["email"]}`)
                let alert = document.getElementById('alert');
                // send email

                // Add class 
                progressBar.style.width = "85%";
                //And change the progress bar color
                progressBar.style.backgroundColor = "red";
                // Change the progress innnerHTML = 100%
                progressBar.innerHTML = "85%";
                
                //Change the innerHTML text = submit
                next.innerHTML = "تسجيل";
            }
            if (!r["message"]["mobile_no_verified"]) {
                appendToUL(`Mobile Number ${r["message"]["mobile_no"]} `)
                progressBar.style.width = "85%";
                //And change the progress bar color
                progressBar.style.backgroundColor = "red";
                // Change the progress innnerHTML = 100%
                progressBar.innerHTML = "85%";
                
                //Change the innerHTML text = submit
                next.innerHTML = "تسجيل";
            }

            }
        },
        freeze: true,
        freeze_message: "Verifying Phone No",
    });
};

const checkEmailVerification = async () => {
    
    const options = await getcheckEmailVerification();

};
next.addEventListener("click", (event) => {

    //Check for step to be displayed 
    if (step1.style.display === "block" && step2.style.display === "none" && step3.style.display === "none") {
        // check if wanna add another person
        // check all fields have value 
        let validDataRespnse = validData(fname, lname, email, phone_no, batchSelect, formAddress, gender, datePicker);
        if (validDataRespnse) {
            frappe.throw("الرجاء ادخال باقي البيانات المطلوبه")
        } else {
        // show popup confirm
        let popup = document.getElementById('popup')
        let yes = document.getElementById('yes')
        let no = document.getElementById('no')
        let windowH = window.innerHeight;
        if (windowH > 720){

            window.scrollTo(0, 620);
        }

        popup.classList.add('open-popup')
        yes.addEventListener("click", (event) => {
            closePopup()
            renderStepTwo()
        })
        no.addEventListener("click", (event) => {
            closePopup()
            renderStepthree()
        })
        
        }
      

      //Check for next (Section) to displayed
    }else if (step2.style.display === "block" && step3.style.display === "none" && step1.style.display === "none" ) {
        let validDataRespnse = validData(fname2, lname2, email2, phone_no2, batchSelectTwo, formAddress2, genderSelectTwo2, datePicker2);
        if (validDataRespnse) {
            frappe.throw("الرجاء ادخال باقي البيانات المطلوبه")
        } else {
            renderStepthree()

        }
        
        
        // Confirm if all steps are completed and then check if inputs are empty
    } else if (step3.style.display === "block" && step2.style.display === "none" && step1.style.display === "none") {
        // check for email and mobile verification 
        // check for email and mobile verification 
        // check for email and mobile verification 
        let validDataRespnse = validData(fname3, favoriteCharacter, datePicker3, genderSelectid, school, favoriteColor, true, true);
        if (validDataRespnse) {
            frappe.throw("الرجاء ادخال باقي البيانات المطلوبه")
        } else {
        

            let stepperForm = document.getElementById("stepper-form").style.display = "none";
                // let title = document.getElementById("main-section").innerHTML = 'لم يتم تفعيلة';
                
                checkEmailVerification()            
                frappe.call({
                    method: "ecs_vim.www.user-details.index.finished_details",
                    callback: function(r){
    
                    },
                    freeze: true,
                    freeze_message: "Verifying Phone No",
                });
                window.location.href = frappe.utils.sanitise_redirect("/customer-details");
                return false;
        }
        // check for email and mobile verification 
            
            } 
    return false;
});

// Back (preview function)
prev.addEventListener("click", () => {
 //Check for active step and add to it a style.display none
  if (step3.style.display === "block" && step2.style.display === "none" && step1.style.display === "none") {
      step1.style.display = "none";
      step2.style.display = "block";
      next.innerHTML = "استمرار";
      next.disabled = false;
      //Set progress bar width
      progressBar.style.backgroundColor = "lightgreen";
      //Set progress bar 
      progressBar.innerHTML = "50%";
      progressBar.style.width = "50%";
      step3.style.display = "none";
    }else if (step3.style.display === "none" && step2.style.display === "block" && step1.style.display === "none") {
        step1.style.display = "block";
        step2.style.display = "none";
        step3.style.display = "none";
        //Set progress bar width
      progressBar.style.backgroundColor = "orange";
      //Set progress bar 
      progressBar.innerHTML = "5%";
      progressBar.style.width = "5%";
    } 
});

/**
 * Function validation
 * this take 3 parameters 
 * and check if is empty 
 */

function validData (a,b,c,d,e,f,g, h){
    if (a.value == "" || b.value == "" || c.value == "" ||d.value == "" || e.value == "" || f.value == "" || g.value == "" || h.value == "") {
       //Add some code here
       next.disabled;
       return true;
    } return false
}


//  relation input drop down list
const batchTrack = document.getElementById("batchSelect");
const getPost = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Family Relation?order_by=order_sequence%20asc");
    const data = response.json();
    return data;
};

const displayOption = async () => {
    const options = await getPost();

    const newOption = document.createElement("option");
    newOption.value = "";
    newOption.text = "";
    batchTrack.appendChild(newOption);
    options.data.forEach(option => {

        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        batchTrack.appendChild(newOption);

    });
};
displayOption();
const genderSelect = document.getElementById("genderSelect");
const getGender = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Gender");
    const data = response.json();
    return data;
};

const displayGender = async () => {
    const options = await getGender();
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        genderSelect.appendChild(newOption);

    });
};
displayGender();

// fetch data second form add another person

//  relation input drop down list
const batchTrackTwo = document.getElementById("batchTrackTwo");
const getPostTwo = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Family Relation?order_by=order_sequence%20asc");
    const data = response.json();
    return data;
};

const displayOptionTwo = async () => {
    const options = await getPostTwo();
    
    const newOption = document.createElement("option");
    newOption.value = "";
    newOption.text = "";
    batchTrackTwo.appendChild(newOption);   
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        batchTrackTwo.appendChild(newOption);

    });
};
displayOptionTwo();
const genderSelectTwo = document.getElementById("genderSelectTwo");
const getGenderTwo = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Gender");
    const data = response.json();
    return data;
};

const displayGenderTwo = async () => {
    const options = await getGenderTwo();
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        genderSelectTwo.appendChild(newOption);

    });
};
displayGenderTwo();

const genderSelectthree = document.getElementById("genderSelectthree");
const getgenderSelectthree = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Gender");
    const data = response.json();
    return data;
};

const displaygenderSelectthree = async () => {
    const options = await getgenderSelectthree();
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        genderSelectthree.appendChild(newOption);

    });
};
displaygenderSelectthree();

const favoriteBranch = document.getElementById("favorite-branch");
const getfavoriteBranch = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Branch");
    const data = response.json();
    return data;
};

const displayfavoriteBranch = async () => {
    const options = await getfavoriteBranch();
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        favoriteBranch.appendChild(newOption);

    });
};
displayfavoriteBranch();

const favoriteBranch2 = document.getElementById("favorite-branch2");
const getfavoriteBranch2 = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Branch");
    const data = response.json();
    return data;
};

const displayfavoriteBranch2 = async () => {
    const options = await getfavoriteBranch2();
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        favoriteBranch2.appendChild(newOption);

    });
};
displayfavoriteBranch2();


const country2 = document.getElementById("country2");
const getcountry2 = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Country?order_by=custom_order_sequence%20asc");
    const data = response.json();
    return data;
};

const displaycountry2 = async () => {
    const options = await getcountry2();
    const newOption = document.createElement("option");
    newOption.value = "";
    newOption.text = "";
    country2.appendChild(newOption);
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        country2.appendChild(newOption);

    });
};
displaycountry2();


const country = document.getElementById("country");
const getcountry = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Country?order_by=custom_order_sequence%20asc");
    const data = response.json();
    return data;
};

const displaycountry = async () => {
    const options = await getcountry();
    const newOption = document.createElement("option");
    newOption.value = "";
    newOption.text = "";
    country.appendChild(newOption);
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        country.appendChild(newOption);

    });
};
displaycountry();


const favorite = document.getElementById("favorite-color");
const getfavorite = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Color");
    const data = response.json();
    return data;
};

const displayfavorite = async () => {
    const options = await getfavorite();
    const newOption = document.createElement("option");
    newOption.value = "";
    newOption.text = "";
    favorite.appendChild(newOption);
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        favorite.appendChild(newOption);

    });
};
displayfavorite();



const favoritechar = document.getElementById("favorite-character");
const getfavoritechar = async () => {
    const response = await fetch("https://erp.vim.sa/api/resource/Cartoon Character");
    const data = response.json();
    return data;
};

const displayfavoritechar = async () => {
    const options = await getfavoritechar();
    const newOption = document.createElement("option");
    newOption.value = "";
    newOption.text = "";
    favoritechar.appendChild(newOption);
    options.data.forEach(option => {
        const newOption = document.createElement("option");
        newOption.value = option.name;
        newOption.text = option.name;
        favoritechar.appendChild(newOption);

    });
};
displayfavoritechar();


// multi select


Array.prototype.search = function(elem) {
    for(var i = 0; i < this.length; i++) {
        if(this[i] == elem) return i;
    }
    
    return -1;
};

var Multiselect = function(selector) {
    if(!$(selector)) {
        console.error("ERROR: Element %s does not exist.", selector);
        return;
    }

    this.selector = selector;
    this.selections = [];

    (function(that) {
        that.events();
    })(this);
};

Multiselect.prototype = {
    open: function(that) {
        var target = $(that).parent().attr("data-target");

        // If we are not keeping track of this one's entries, then
        // start doing so.
        if(!this.selections) {
            this.selections = [ ];
        }

        $(this.selector + ".multiselect").toggleClass("active");
    },

    close: function() {
        $(this.selector + ".multiselect").removeClass("active");
    },

    events: function() {
        var that = this;

        $(document).on("click", that.selector + ".multiselect > .title", function(e) {
            if(e.target.className.indexOf("close-icon") < 0) {
                that.open();
            }
        });

        $(document).on("click", that.selector + ".multiselect option", function(e) {
            var selection = $(this).attr("value");
            var target = $(this).parent().parent().attr("data-target");

            var io = that.selections.search(selection);

            if(io < 0) that.selections.push(selection);
            else that.selections.splice(io, 1);

            that.selectionStatus();
            that.setSelectionsString();
        });

        $(document).on("click", that.selector + ".multiselect > .title > .close-icon", function(e) {
            that.clearSelections();
        });

        $(document).click(function(e) {
            if(e.target.className.indexOf("title") < 0) {
                if(e.target.className.indexOf("text") < 0) {
                    if(e.target.className.indexOf("-icon") < 0) {
                        if(e.target.className.indexOf("selected") < 0 ||
                           e.target.localName != "option") {
                            that.close();
                        }
                    }
                }
            }
        });
    },

    selectionStatus: function() {
        var obj = $(this.selector + ".multiselect");

        if(this.selections.length) obj.addClass("selection");
        else obj.removeClass("selection");
    },

    clearSelections: function() {
        this.selections = [];
        this.selectionStatus();
        this.setSelectionsString();
    },

    getSelections: function() {
        return this.selections;
    },

    setSelectionsString: function() {
        var selects = this.getSelectionsString().split(", ");
        $(this.selector + ".multiselect > .title").attr("title", selects);

        var opts = $(this.selector + ".multiselect option");

        if(selects.length > 6) {
            var _selects = this.getSelectionsString().split(", ");
            _selects = _selects.splice(0, 6);
            $(this.selector + ".multiselect > .title > .text")
                .text(_selects + " [...]");
        }
        else {
            $(this.selector + ".multiselect > .title > .text")
                .text(selects);
        }

        for(var i = 0; i < opts.length; i++) {
            $(opts[i]).removeClass("selected");
        }

        for(var j = 0; j < selects.length; j++) {
            var select = selects[j];

            for(var i = 0; i < opts.length; i++) {
                if($(opts[i]).attr("value") == select) {
                    $(opts[i]).addClass("selected");
                    break;
                }
            }
        }
    },

    getSelectionsString: function() {
        if(this.selections.length > 0)
            return this.selections.join(", ");
        else return "Select";
    },

    setSelections: function(arr) {
        if(!arr[0]) {
            error("ERROR: This does not look like an array.");
            return;
        }

        this.selections = arr;
        this.selectionStatus();
        this.setSelectionsString();
    },
};

$(document).ready(function() {
    var multi = new Multiselect("#countries");
});


// date 
