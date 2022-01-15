//Script to Top Borrow Slider
window.addEventListener("load", function(){
    const slider = document.querySelector(".nSlick-list");
    const sliderMain = document.querySelector(".nSlick-track");
    const sliderItems = document.querySelectorAll(".nSlick-slide");
    const nextBtn = document.querySelector(".nSlider-next");
    nextBtn.style = `cursor:pointer`;
    const prevBtn = document.querySelector(".nSlider-prev");
    prevBtn.style = `opacity: 0`;
    const sliderItemWidth = sliderItems[0].offsetWidth;
    const sliderLength = sliderItems.length;
    let positionX = 0;
    let index = 0;
    console.log(sliderItems.length);

    nextBtn.addEventListener("click", function(){
        handleChangSlide(1);
    });

    prevBtn.addEventListener("click", function(){
        handleChangSlide(-1);
    });

    function handleChangSlide(direction) {
        if (direction == 1) {
            if (index >= sliderLength - 5) {
                index = sliderLength - 5;
                positionX = - sliderItemWidth*(sliderLength - 5);
                return;    
            } else index++;
            positionX = positionX - sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        else if (direction == -1) {
            if (index <= 0) {
                index = 0;
                positionX = 0;
                return;    
            } else index--;
            positionX = positionX + sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        if (index <= 0) {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 0`;
            nextBtn.style = `cursor:pointer`;
        }
        else if (index >= sliderLength - 5) {
            nextBtn.style = `opacity: 0`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
        } else {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
            nextBtn.style = `cursor:pointer`;
        }
    }
});

//Script to Top Borrow Slider
window.addEventListener("load", function(){
    const slider = document.querySelector(".rvSlick-list");
    const sliderMain = document.querySelector(".rvSlick-track");
    const sliderItems = document.querySelectorAll(".rvSlick-slide");
    const nextBtn = document.querySelector(".rvSlider-next");
    nextBtn.style = `cursor:pointer`;
    const prevBtn = document.querySelector(".rvSlider-prev");
    prevBtn.style = `opacity: 0`;
    const sliderItemWidth = sliderItems[0].offsetWidth;
    const sliderLength = sliderItems.length;
    let positionX = 0;
    let index = 0;
    console.log(sliderItems.length);

    nextBtn.addEventListener("click", function(){
        handleChangSlide(1);
    });

    prevBtn.addEventListener("click", function(){
        handleChangSlide(-1);
    });

    function handleChangSlide(direction) {
        if (direction == 1) {
            if (index >= sliderLength - 5) {
                index = sliderLength - 5;
                positionX = - sliderItemWidth*(sliderLength - 5);
                return;    
            } else index++;
            positionX = positionX - sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        else if (direction == -1) {
            if (index <= 0) {
                index = 0;
                positionX = 0;
                return;    
            } else index--;
            positionX = positionX + sliderItemWidth;
            sliderMain.style = `transform: translateX(${positionX}px)`;
            // console.log(index);
            // console.log(sliderItemWidth);
            // console.log(positionX);
        }
        if (index <= 0) {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 0`;
            nextBtn.style = `cursor:pointer`;
        }
        else if (index >= sliderLength - 5) {
            nextBtn.style = `opacity: 0`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
        } else {
            nextBtn.style = `opacity: 1`;
            prevBtn.style = `opacity: 1`;
            prevBtn.style = `cursor:pointer`;
            nextBtn.style = `cursor:pointer`;
        }
    }
});