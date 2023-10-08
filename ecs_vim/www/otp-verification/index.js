let frappe_call = (args) => {
    frappe.call({
        method: args.cmd,
        args: {
            "otp":args.otp,
            "session_doc":args.session_doc,

        },
        callback: function(r) {
            if (r) {
                if (r.message[0].status == "V") {
                    window.location.href = frappe.utils.sanitise_redirect(r.message[1]);

                } else {
                    alert(r.message[0].remarks)
                }

            }
        },
        freeze: true,
        freeze_message: "Verifying Phone No",
    });

}
$(".form-otp").on("submit", function (event) {
    event.preventDefault();
    var args = {};
    args.cmd = "ecs_vim.www.otp-verification.index.verify_otp";
    args.otp = $("#otp").val();
    args.session_doc =  window.location.href.split("/").at(-1);
    frappe_call(args);
    return false;
});