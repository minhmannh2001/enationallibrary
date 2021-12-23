//Script to Relevant Book
window.addEventListener("load", function(){
    const slider = document.querySelector(".rbBookList");
    const sliderMain = document.querySelector(".rbSlick-track");
    const sliderItems = document.querySelectorAll(".rbSlick-slide");
    const nextBtn = document.querySelector(".rbSlider-next");
    nextBtn.style = `cursor:pointer`;
    const prevBtn = document.querySelector(".rbSlider-prev");
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
            if (index >= sliderLength - 6) {
                index = sliderLength - 6;
                positionX = - sliderItemWidth*(sliderLength - 6);
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
        else if (index >= sliderLength - 6) {
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

//Script to From the Author
window.addEventListener("load", function(){
    const slider = document.querySelector(".faBookList");
    const sliderMain = document.querySelector(".faSlick-track");
    const sliderItems = document.querySelectorAll(".faSlick-slide");
    const nextBtn = document.querySelector(".faSlider-next");
    nextBtn.style = `cursor:pointer`;
    const prevBtn = document.querySelector(".faSlider-prev");
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
            if (index >= sliderLength - 6) {
                index = sliderLength - 6;
                positionX = - sliderItemWidth*(sliderLength - 6);
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
        else if (index >= sliderLength - 6) {
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
