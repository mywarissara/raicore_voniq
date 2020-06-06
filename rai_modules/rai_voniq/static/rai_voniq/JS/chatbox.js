// function openForm() {
//     document.getElementById("myForm").style.display = "block";
// }

// function closeForm() {
//     document.getElementById("myForm").style.display = "none";
// }

// (function() { // “immediately-invoked function expressions” (IIFE).

// var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
// var recognition = new SpeechRecognition(); //created an instantiation of the speech recognition interface.
// var Textbox = $('.message_input'); //hold the text for display after the speech is converted to text.
// var Content = '';

// var result = bowser.getParser(navigator.userAgent).getResult(); //@var {class} result Get the data about bowser
// console.log(result.browser.name)

// result.browser.name == "Chrome" ? $(".send_message").show() : $(".send_message").hide(); // use voice only Chrome

// var Message = function(arg) { // function expression
//     this.text = arg.text, this.message_side = arg.message_side;
//     this.draw = function(_this) {
//         return function() {
//             var $message;
//             $message = $($('.message_template').clone().html());
//             $message.addClass(_this.message_side).find('.text').html(_this.text);
//             $('.messages').append($message);
//             return setTimeout(function() {
//                 return $message.addClass('appeared');
//             }, 0);
//         };
//     }(this);
//     return this;
// };

// $(function() {
// var getMessageText, message_side, sendMessage;

// recognition.continuous = true;
// recognition.onresult = function(e) {
//     Content = ''
//     var current = event.resultIndex;
//     var transcript = event.results[current][0].transcript;
//     Content += transcript;
//     Textbox.val(Content);
//     enterMessageText(e);
// };

// if (Content.length) {
//     Content += ' ';
// }

// Textbox.on('input', function() {
//     Content = $(this).val();
// })

// getMessageText = function() {
//     var $message_input;
//     $message_input = $('.message_input');
//     return $message_input.val();
// };

// sendMessage = function(text, isLeft) {
//     var $messages, message;
//     if (text.trim() === '') {
//         return;
//     }
//     $('.message_input').val('');
//     $messages = $('.messages');
//     message = new Message({
//         text: text,
//         message_side: isLeft
//     });
//     message.draw();
//     return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
// };

// var enterMessageText = function(e) {

//     var inputMassage = getMessageText();

//     sendMessage(inputMassage, 'right');

//     const Http = new XMLHttpRequest();
//     const url = (window.location.protocol + "//" + window.location.hostname + '/modules/voniq/passPara/?message=' + inputMassage);
//     //console.log(url);
//     Http.open("GET", url);
//     Http.send();
//     Http.onreadystatechange = (e) => {
//         if (Http.readyState == 4 && Http.status == 200) {
//             recognition.stop();
//             readOutLoud(Http.responseText)
//             sendMessage(Http.responseText, 'left');
//             setTimeout(function() {
//                 recognition.start();
//             }, 3500);
//         }
//     }
// }

// $('.send_message').click(function(e) {
//     recognition.start();
// });

// $('.message_input').keyup(function(e) {
//     if (e.which === 13) {
//         enterMessageText(e);
//     }
// });

// function readOutLoud(message) {
//     var speech = new SpeechSynthesisUtterance();
//     // Set the text and voice attributes.
//     speech.text = message;
//     speech.volume = 1;
//     speech.rate = 1;
//     speech.pitch = 1;

//     window.speechSynthesis.speak(speech);
// }
// });
// }.call(this));