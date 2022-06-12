class key{
    constructor(letter){
        this.letter=letter;
        this.x=null;
        this.y=null;
        this.state=0;
        this.submitted = false;
        this.w=null;
        this.wref=null;
        this.sw=0;
        this.col=color(217,217,217);
    }

    show(){
        rectMode(CENTER);
        fill(this.col);
        stroke(0);
        strokeWeight(this.sw);
        rect(this.x ,this.y,this.w,this.w,0.012*height);
        fill(0);
        stroke(0);
        strokeWeight(0.5);
        textAlign(CENTER,CENTER);
        textSize(0.018*height);
        text(this.letter,this.x,this.y);
    }

    hovered(){
        if ((mouseX>=this.x-this.w/2)&(mouseX<=this.x+this.w/2)&(mouseY>=this.y-this.w/2)&(mouseY<=this.y+this.w/2)) {
            return true;
        }
        return false;
    }

    isClicked(){
        if (!["ENTER","DEL"].includes(this.letter)) {
            addLetter(this.letter);
        }
        else if (this.letter=="ENTER") {
            guessWord();
        }
        else if (this.letter=="DEL") {
            removeLetter();
        }
    }

    update(){
        if (this.hovered()) {
            this.sw=3;
        }
        else{
            this.sw=0;
        }
        switch (this.state) {
            case 1:
                this.col = color(100,100,100);
                break;
            case 2:
                this.col = color(235,200,120);
                break;
            case 3:
                this.col = color(150,235,120);
                break;
            default:
                break;
        }
    }

    updatePL(){
        if (this.hovered()) {
            this.sw=3;
        }
        else{
            this.sw=0;
        }
        switch (this.state) {
            case 3:
                this.col = color(226, 28, 38);
                break;
            case 2:
                
                this.col = color(249, 141, 143);
                break;
            case 1:
                
                this.col = color(100,100,100);
                break;
            
            default:
                break;
        }

    }

}