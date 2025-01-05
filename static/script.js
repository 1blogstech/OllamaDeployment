let i = 1;
let x = 1;
async function sendBtn(){
    text_input = document.getElementById("message-input")
    chat_area = document.getElementById("chat-window")
    sendbtn = document.getElementById("send-button")
    
    const currentDate = new Date();
    const hours = currentDate.getHours();
    const minutes = currentDate.getMinutes();
    const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
    value = text_input.value
    if (text_input.value){
        chat_area.innerHTML += `
        <div class="chat-message user">
            <div class="message" id="user${x}">${text_input.value}<div class="time prevent-select">${formattedTime}</div></div>
        </div>`
        x+=1
        text_input.value = ""
        sendbtn.disabled=true
        chat_area.innerHTML += `
        <div class="chat-message bot">
            <img src="static/Ollama.png" alt="Ollama" id="ollama_loading" width="30px">
            <img id="loading" src="static/loading.gif" width="50px">
        </div>
        `
        
        loading = document.getElementById("loading")
        Ollamaloading = document.getElementById("ollama_loading")
        
        try {
                const response = await fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ message: value }),
                });

                if (response.ok) {
                    const data = await response.json();
                    const botResponse = data.response.replace(/\n/g, '<br>');
                    loading.remove()
                    Ollamaloading.remove()
                    chat_area.innerHTML +=`
                    <div class="chat-message bot">
                        <img src="static/Ollama.png" alt="Ollama" width="30px">
                        <div class="message" id="chatbot${i}">${botResponse}<div class="time prevent-select">${formattedTime}</div></div>
                    </div>`
                    
                    // Display Ollama's response
    
                    sendbtn.disabled=false
                    chat_area.scrollTop = chat_area.scrollHeight;
                    i+=1
                    
                    // Scroll to the bottom of the chatbox
                    //chatBox.scrollTop = chatBox.scrollHeight;
                    
                }
            }
            catch (error) {
                console.error("Error:", error);
            }
        }
    }
