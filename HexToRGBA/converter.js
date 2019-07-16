var htorgba = function (hexColor){

	if(typeof hexColor !== 'string'){
      return 'Invalid Hex Code Not String';
    }
    else{
    hexColor = hexColor.replace('#','');
    var red,green,blue,alpha;
    	if(hexColor.length == 8)
      {
        red = hexColor.substring(0,2);
        green = hexColor.substring(2,4);
        blue = hexColor.substring(4,6);
        alpha = hexColor.substring(6,8);

        
      }
      else if((hexColor.length) <8 && (hexColor.length) == 3){
      	 red = hexColor.substring(0,1);
         red = red + red;
         green = hexColor.substring(1,2);
         green = green + green;
         blue = hexColor.substring(2,3);
         blue = blue + blue;
         
         alpha = 100;
         
         
      }
      else if((hexColor.length) <8 && (hexColor.length) == 4){
      	 red = hexColor.substring(0,1);
         red = red + red;
         green = hexColor.substring(1,2);
         green = green + green;
         blue = hexColor.substring(2,3);
         blue = blue + blue;
         alpha = hexColor.substring(3,4);
         alpha = alpha + alpha;
      }
      else if((hexColor.length) <8 && (hexColor.length) == 6){
        red = hexColor.substring(0,2);
        green = hexColor.substring(2,4);
        blue = hexColor.substring(4,6);
        
        alpha = 100;
        
        
     }
      else{
      	return "Invalid Hex Code Not Good Format";
      }
      red = parseInt(red,16);
      green = parseInt(green,16);
      blue = parseInt(blue,16);
      alpha = parseInt(alpha,10);
      alpha = alpha/100;

      if(isNaN(red) || isNaN(green) || isNaN(blue) || isNaN(alpha)){

        return "Invalid Hex Code NaN";
      }
      
      return "rgba("+red+","+green+","+blue+","+alpha+")";
    }

}
module.exports = {
    HexToRGBA:htorgba
};
