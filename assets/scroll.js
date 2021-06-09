let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);

window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        scrollHijack: function(pathname) {
            if(pathname === "/apps/itesm")
                document.body.style.overflowY = "hidden";
            else
                document.body.style.overflowY = "auto";
        }
    }
});

const navDispatch = (event) => {
    const keyName = event.key;
    numSections = document.getElementsByClassName("page-section").length

    // TODO
    // Grab window.location, mutate it and
    // navigate to it with similar logic to the button Python
    // code
    let currentAnchor = window.location.hash;
    let next_a, prev_a;

    // If the currentAnchor is empty, it means we've just loaded
    // the page
    if(currentAnchor === "") {
        next_a = 1
        prev_a = 0
    }
    else {
        // If it's not, then we have to extract the section number
        currentSection = parseInt(currentAnchor.match(/\d\d?/)[0])
        prev_a = currentSection == 0 ? 0 : currentSection - 1;
        next_a = currentSection == numSections - 1 ? currentSection : currentSection + 1;
    }

    if(keyName === 'ArrowDown') {
        window.location.hash = `#section-${next_a}-up`
    }
    else if(keyName === 'ArrowUp') {
        window.location.hash = `#section-${prev_a}-up`
    }
}

window.addEventListener('resize', () => {
    let vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
})

document.addEventListener('keydown', navDispatch)
window.addEventListener('load', () => {
    numSections = document.getElementsByClassName("page-section").length
    console.log(numSections)
    console.log("loaded")
});
