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


        // ---------------To handle logout form
        const logoutForm = document.querySelector("#logout-form") || null;

        console.log("this is form", logoutForm);

        if (logoutForm) {
            logoutForm.addEventListener("submit",
                function (event) {
                    const userConfirmed = confirm("Are you sure to logout ? ");

                    if (!userConfirmed) {
                        event.preventDefault();
                    }
                });
        }

        /* if (logoutForm) {
            logoutForm.addEventListener("submit", function (event) {
                console.log("Submit button clicked");
                const userConfirmed = confirm("Are you sure you want to logout?");
                if (!userConfirmed) {
                    event.preventDefault();
                }
            });
        } */
    }
};


document.addEventListener("DOMContentLoaded", initApp);