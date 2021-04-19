const expect = require('chai').expect;
const fizzBuzz = require('../fizzBuzz.js');
describe('FizzBuzz >', () => {
it('OK, FizzBuzz returns 1', () => {
    expect(fizzBuzz(1)).to.equal(1);
})
});