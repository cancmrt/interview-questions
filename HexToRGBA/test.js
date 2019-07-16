var assert = require('assert');
var convert = require('./converter');
console.log(convert);
describe("Basic test of hex to RGBA", function(){

    it('Should return rgba(255,255,255,1) Input:FFF',function(){
        assert.equal(convert.HexToRGBA('FFF'),'rgba(255,255,255,1)');
    });
    it('Should return rgba(255,255,255,1) Input:#FFF',function(){
        assert.equal(convert.HexToRGBA('#FFF'),'rgba(255,255,255,1)');
    });
    it('Should return rgba(255,255,255,1) Input:#FFFFFF',function(){
        assert.equal(convert.HexToRGBA('#FFFFFF'),'rgba(255,255,255,1)');
    });
    it('Should return rgba(255,255,255,1) Input:FFFFFF',function(){
        assert.equal(convert.HexToRGBA('FFFFFF'),'rgba(255,255,255,1)');
    });
    it('Should return rgba(255,255,255,1) Input:#FFF5',function(){
        assert.equal(convert.HexToRGBA('#FFF5'),'rgba(255,255,255,0.55)');
    });
    it('Should return rgba(255,255,255,1) Input:FFF3',function(){
        assert.equal(convert.HexToRGBA('FFF3'),'rgba(255,255,255,0.33)');
    });
    it('Should return rgba(255,255,255,1) Input:#FFFF',function(){
        assert.equal(convert.HexToRGBA('FFF'),'rgba(255,255,255,1)');
    });
    it('Should return Invalid Hex Code NaN Input:#FFFF',function(){
        assert.equal(convert.HexToRGBA('FFFF'),'Invalid Hex Code NaN');
    });
    it('Should return Invalid Hex Code Not Good Format Input:#FFFFFFFFFFF',function(){
        assert.equal(convert.HexToRGBA('#FFFFFFFFFFF'),'Invalid Hex Code Not Good Format');
    });
    it('Should return Invalid Hex Code Not String Input:123456',function(){
        assert.equal(convert.HexToRGBA(123456),'Invalid Hex Code Not String');
    });


})
