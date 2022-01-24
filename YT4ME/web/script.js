
const recent = document.querySelector(".mid");
const result = document.querySelector(".random_number");

document.querySelector("button").onclick = function () {
    result.innerHTML = "<strong>다운로드 중...</strong>"
    fileName = document.querySelector("input").value;
    eel.download_mp3(fileName)(function(TITLE){
        result.innerHTML = TITLE ? `<strong>다운로드 완료</strong><p>${TITLE}</p>`: `<strong>다운로드 실패</strong>`
        draw_recent();
    })
}


function draw_recent() {
    eel.recent_mp3()(function(LIST){
        returnHTML = "<ul>"
        for(i=0; i<LIST.length; i++) {
            returnHTML += 
            `<li>${LIST[i]}</li>`;
        }
        returnHTML += "</ul>"
        recent.innerHTML = returnHTML;
    })
}

draw_recent();

