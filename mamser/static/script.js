//STUDENT CONFIGURATION SECTION
var currentStudConfigNavbarLogo = document.getElementById("navbarLogo-add");
var currentStudConfigDisplay = document.getElementById("addRegistry");

var studInfo = new Array(4);

function studConfig(logo, registry) {
    currentStudConfigDisplay.style.display = "none";
    currentStudConfigNavbarLogo.style.margin = "12.5px";
    currentStudConfigNavbarLogo.style.width = "30px";
    currentStudConfigNavbarLogo.style.fill = "white";
    currentStudConfigNavbarLogo = document.getElementById(logo);
    document.getElementById(registry).style.display = "block";
    currentStudConfigNavbarLogo.style.margin = "10px";
    currentStudConfigNavbarLogo.style.width = "35px";
    currentStudConfigNavbarLogo.style.fill = "#C8530C";
    currentStudConfigDisplay = document.getElementById(registry);
}

studConfig("navbarLogo-add", "addRegistry");

document.getElementById("navbarLogo-addCont").onclick = function() {
    studConfig("navbarLogo-add", "addRegistry");
}
document.getElementById("navbarLogo-deleteCont").onclick = function() {
    studConfig("navbarLogo-delete", "deleteRegistry");
}
document.getElementById("navbarLogo-searchCont").onclick = function() {
    studConfig("navbarLogo-search", "searchRegistry");
}

//ADD REGISTRY
document.getElementById("add_course").style.display = "none";
document.getElementById("add_college").firstChild.setAttribute("disabled", "true");
document.getElementById("add_college").firstChild.setAttribute("hidden", "true");

let add_college_select = document.getElementById("add_college");
let add_course_select = document.getElementById("add_course");

add_college_select.onchange = function() {
    add_course_select.style.display = "block";
    add_college_id = add_college_select.value;
    
    fetch("/coursesoptionlib/" + add_college_id).then(function(response) {
        response.json().then(function(data) {
            let addOptionHTML = "";

            for (let course of data.courses) {
                addOptionHTML += '<option value="' + course.db_id + '">' + course.name + '</option>';
            }
            add_course_select.innerHTML = addOptionHTML;
        });

    });
}

//SEARCH REGISTRY
let search_college_select = document.getElementById("search_college");
let search_course_select = document.getElementById("search_course");

search_course_select.style.display = "none";
search_college_select.firstChild.setAttribute("disabled", "true");
search_college_select.firstChild.setAttribute("hidden", "true");

search_college_select.onchange = function() {
    search_course_select.style.display = "block";
    search_college_id = search_college_select.value;
    
    fetch("/coursesoptionlib/" + search_college_id).then(function(response) {
        response.json().then(function(data) {
            let searchOptionHTML = "";

            for (let course of data.courses) {
                searchOptionHTML += '<option value="' + course.db_id + '">' + course.name + '</option>';
            }
            search_course_select.innerHTML = searchOptionHTML;
        });

    });
}

let content = document.getElementById("student_list");
let search_button = document.getElementById("search_submit");

search_button.onclick = function() {
    content.innerHTML = ""
    search_student_idNo = document.getElementById("search_idNo").value;

    fetch("/studentsearchidnolib/" + search_student_idNo).then(function(response) {
        response.json().then(function(data) {
            if(data.student.idNo != undefined){
                let content_html = "";  
                content_html += '<p>' + data.student.idNo + ", " + data.student.name + ", " + data.student.gender + ", " + data.student.course + ", " + data.student.college + '</p><br>';
                content.innerHTML = content_html;
            }
        })
    })
}


