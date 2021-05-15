let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        scrollSection: function() {
            console.log("in scrollSection")
            direction =
                JSON.parse(
                    dash_clientside
                        .callback_context
                        .triggered[0]
                        .prop_id
                        .replace(/\.n_clicks/, "")
                ).direction

            factor = direction == "up" ? -1 : 1;

            window.scrollBy({
                top: factor * document.documentElement.clientHeight,
                behavior: "smooth"
            });
        },
        scrollHijack: function(pathname) {
            if(pathname === "/apps/itesm")
                document.body.style.overflowY = "hidden";
            else
                document.body.style.overflowY = "auto";
        }
    }
});

window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
})
