// let toDo = [];

// while (true) {
//     let req = prompt("Please enter your request");

//     if (req === "quit") {
//         console.log("Closing application");
//         break;
//     }
//     if (req === "list") {
//         console.log("----------");
//         if (toDo.length === 0) {
//             console.log("No activities to show.");
//         } else {
//             for (let i = 0; i < toDo.length; i++) {
//                 console.log(i + 1, toDo[i]);
//             }
//         }
//         console.log("----------");
//     }
//     else if (req === "add") {
//         let act = prompt("Enter the activity you want to add");
//         if (act) {
//             toDo.push(act);
//             console.log("Activity added");
//         } else {
//             console.log("No activity entered");
//         }
//     }
//     else if (req === "delete") {
//         let index = parseInt(prompt("Enter the activity's serial number you want to delete"), 10);
//         if (isNaN(index) || index < 1 || index > toDo.length) {
//             console.log("Invalid serial number");
//         } else {
//             let dact = toDo.splice(index - 1, 1);
//             console.log(`${dact} deleted`);
//         }
//     }
//     else {
//         console.log("Invalid request");
//     }
// }
