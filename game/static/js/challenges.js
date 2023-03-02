let tasks = ["recycle at bin 1", "walk green trails", "walk 2km"];

// Function to create the tasks
function createTasks() {
    // Get the element with the ID "tasks"
    let tasksContainer = document.getElementById("tasks");

    // Loop through the tasks array and create a new task for each task
    for (let i = 0; i < tasks.length; i++) {
        let task = tasks[i];

        // Create a new task element
        let taskElement = document.createElement("div");
        taskElement.classList.add("task");

        // Create a new label element for the task
        let label = document.createElement("label");
        label.appendChild(document.createTextNode(task));

        // Create a new button element for marking the task as done
        let button = document.createElement("button");
        button.appendChild(document.createTextNode("Done"));

        // Add an event listener to the button to mark the task as done
        if (task === "walk green trails") {
            button.addEventListener("click", function () {
                window.location.href = "http://127.0.0.1:8000/map/";

            });

        } else {
            button.addEventListener("click", function () {
                taskElement.parentNode.removeChild(taskElement);
            });
        }

        // Add the label and button to the task element
        taskElement.appendChild(label);
        taskElement.appendChild(button);

        // Add the task element to the tasks container
        tasksContainer.appendChild(taskElement);
    }

}

     