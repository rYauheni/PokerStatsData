function copyToClipboard() {
              var copyText = document.getElementById("data-to-copy").innerText; // получаем текст элемента, содержащий данные, которые нужно скопировать
              var textArea = document.createElement("textarea"); // создаем временный элемент textarea
              textArea.value = copyText; // присваиваем значение текста, который нужно скопировать
              document.body.appendChild(textArea); // добавляем textarea в DOM
              textArea.select(); // выделяем текст в textarea
              document.execCommand("copy"); // копируем текст в буфер обмена
              document.body.removeChild(textArea); // удаляем textarea из DOM
            }
