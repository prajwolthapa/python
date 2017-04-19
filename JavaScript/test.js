// Function and Scope 


function Square(dim){
    this.dim = dim
};
    Square.prototype.getArea = function(){
        return Math.imul(this.dim * this.dim)

    };



var newsquare = new Square(5);
console.log(newsquare.getArea())