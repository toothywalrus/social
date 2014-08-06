'use strict';

describe('Service: ACCESSLEVELS', function () {

  // load the service's module
  beforeEach(module('tryApp'));

  // instantiate service
  var ACCESSLEVELS;
  beforeEach(inject(function (_ACCESSLEVELS_) {
    ACCESSLEVELS = _ACCESSLEVELS_;
  }));

  it('should do something', function () {
    expect(!!ACCESSLEVELS).toBe(true);
  });

});
