let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        scrollSection: function() {
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
                top: factor * window.innerHeight,
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

const scroll = (factor) => {
    window.scrollBy({
        top: factor * window.innerHeight,
        behavior: "smooth"
    });
}

window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
})

document.addEventListener('keydown', async (event) => {
    const keyName = event.key;

    if(keyName === 'ArrowDown') {
        scroll(1);
    }
    else if(keyName === 'ArrowUp') {
        scroll(-1);
    }
})
