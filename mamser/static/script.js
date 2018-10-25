//STUDENT CONFIGURATION SECTION
var currentStudConfigNavbarLogo = document.getElementById("navbarLogo-search");
var currentStudConfigDisplay = document.getElementById("searchRegistry");

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

document.getElementById("navbarLogo-addCont").onclick = function() {
    studConfig("navbarLogo-add", "addRegistry");
}
document.getElementById("navbarLogo-deleteCont").onclick = function() {
    studConfig("navbarLogo-delete", "deleteRegistry");
}
document.getElementById("navbarLogo-searchCont").onclick = function() {
    studConfig("navbarLogo-search", "searchRegistry");
}

let content = document.getElementById("viewbox-content");
let idNo_search_button = document.getElementById("idNo_search_submit");

idNo_search_button.onclick = function() {
    content.innerHTML = "";
    search_student_idNo = document.getElementById("search_idNo").value;
    fetch("/idnosearch/" + search_student_idNo).then(function(response) {
        response.json().then(function(data) {
            if(data.student.idNo != undefined){
                let content_html = "";
                content_html += '<table class="table table-hover"><tbody><tr><th scope="row">1</th><td>' + data.student.idNo + '</td><td>' + data.student.name + '</td><td>' + data.student.gender + '</td><td>' + data.student.college + '</td><td>' + data.student.course + '</td></tr></tbody></table>';

                content.innerHTML = content_html;
            }
        })
    })
}

let gender_search_button = document.getElementById("gender_search_submit");

gender_search_button.onclick = function() {
    let gender_options = ["Male", "Female"];
    content.innerHTML = "";
    search_student_gender = document.getElementsByName("gender");
    for(var i=0, length=search_student_gender.length; i<length; i++) {
        if (search_student_gender[i].checked) {

            fetch("/gendersearch/" + gender_options[i]).then(function(response) {
                response.json().then(function(data) {
                    let content_html = '<table class="table table-hover"><tbody>';
                    let count = 1;
                    for(let student of data.students) {
                        if(student.idNo != undefined){
                            content_html += '<tr><th scope="row">' + count + '</th><td>' + student.idNo + '</td><td>' + student.name + '</td><td>' + student.gender + '</td><td>' + student.college + '</td><td>' + student.course + '</td></tr>';
                            count++;
                        }
                    }
                    if(count <= 100) {
                        for(var i=count; i<=100; i++) {
                            content_html += '<tr><th scope="row">' + i + '</th></tr>';
                        }
                        content_html += '</tbody></table>';
                        content.innerHTML = content_html;
                    }
                    else if(count > 100 && count <= 1000) {
                        for(var i=count; i<=1000; i++) {
                            content_html += '<tr><th scope="row">' + i + '</th></tr>';
                        }
                        content_html += '</tbody></table>';
                        content.innerHTML = content_html;
                    }
                    else {
                        for(var i=count; i<=10000; i++) {
                            content_html += '<tr><th scope="row">' + i + '</th></tr>';
                        }
                        content_html += '</tbody></table>';
                        content.innerHTML = content_html;
                    }
                })
            })
        }
    }
}

document.getElementById("add_course").style.display = "none";
document.getElementById("add_college").firstChild.setAttribute("disabled", "true");
document.getElementById("add_college").firstChild.setAttribute("hidden", "true");

let add_college_select = document.getElementById("add_college");
let add_course_select = document.getElementById("add_course");

add_college_select.onchange = function() {
    add_course_select.style.display = "block";
    add_college_id = add_college_select.value;
    
    fetch("/courseoptions/" + add_college_id).then(function(response) {
        response.json().then(function(data) {
            let addOptionHTML = "";

            for (let course of data.courses) {
                addOptionHTML += '<option value="' + course.db_id + '">' + course.name + '</option>';
            }
            add_course_select.innerHTML = addOptionHTML;
        });

    });
}