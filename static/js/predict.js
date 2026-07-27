console.log("Predict.js Loaded");


const symptoms = window.symptoms || [];


const search = document.getElementById("symptomSearch");
const dropdown = document.getElementById("symptomDropdown");
const selectedBox = document.getElementById("selectedSymptoms");
const hiddenInputs = document.getElementById("hiddenInputs");


let selected = [];


// Search symptoms
search.addEventListener("input", () => {

    let value = search.value.toLowerCase().trim();

    dropdown.innerHTML = "";


    if (value.length < 2) {
        return;
    }


    let results = symptoms.filter(symptom =>

        symptom.toLowerCase().includes(value)
        &&
        !selected.includes(symptom)

    );


    results.slice(0, 8).forEach(symptom => {


        let item = document.createElement("div");

        item.className = "symptom-option";

        item.innerText = symptom;



        item.onclick = function () {

           console.log("Clicked:", symptom);

           addSymptom(symptom);

            console.log("Selected:", selected);

            console.log(hiddenInputs.innerHTML);

          search.value = "";
          dropdown.innerHTML = "";
};


        dropdown.appendChild(item);


    });


});





function addSymptom(symptom){

    if(selected.includes(symptom)){
        return;
    }

    if(selected.length >= 10){
        alert("Please select maximum 10 symptoms");
        return;
    }

    selected.push(symptom);

    // ================= CHIP =================

    let chip = document.createElement("span");

    chip.className = "symptom-chip";

    chip.id = "chip-" + symptom.replace(/\W/g,"_");

    chip.innerHTML = `
        ${symptom}
        <button type="button">×</button>
    `;

    chip.querySelector("button").onclick = function(){

        removeSymptom(symptom, chip);

    };

    selectedBox.appendChild(chip);

    // ================= HIDDEN INPUT =================

    let input = document.createElement("input");

    input.type = "hidden";

    input.name = symptom;

    input.value = "1";

    input.id = "input-" + symptom.replace(/\W/g,"_");

    hiddenInputs.appendChild(input);

    console.log("Added:", symptom);
}




// Remove symptom

function removeSymptom(symptom, chip){


    selected = selected.filter(
        item => item !== symptom
    );



    let input = document.getElementById(
        "input-" + symptom.replace(/\W/g,"_")
    );


    if(input){

        input.remove();

    }



    chip.remove();


}