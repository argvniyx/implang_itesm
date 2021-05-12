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
                top: factor * document.documentElement.clientHeight,
                behavior: "smooth"
            });
        }
    }
});
