const initApp = () => {

    const msgContent = document.querySelector("#message") || null;

    const errorMsgContent = document.querySelector(".error-msg") || null;

    if (msgContent || errorMsgContent) {

        const msgContainer = msgContent ? msgContent.parentNode : errorMsgContent.parentNode;


        console.log("this is msg container::", msgContainer);

        setTimeout(() => {

            msgContainer.removeChild(msgContent || errorMsgContent);
            console.log("message is removed successfully.");
            /* if (msgContent) {
                msgContainer.removeChild(msgContent);
            } else {
                msgContainer.removeChild(errorMsgContent);

            } */
        }, 3000);

    }

    // ---------------To handle form
    const logoutForm = document.querySelector("#logout-form") || null;

    const deleteProductForm = document.querySelector("#delete-product") || null;


    function handleForm(element, label = "") {
        console.log("this is element", element);

        if (element) {
            element.addEventListener("submit", function (event) {
                const userConfirmed = confirm(`Are you sure to ${label} ?`);

                if (!userConfirmed) {
                    event.preventDefault();
                }
            });
        }
    }

    

    

    handleForm(logoutForm, 'logout');
    handleForm(deleteProductForm, 'delete this item');






};





document.addEventListener("DOMContentLoaded", initApp);