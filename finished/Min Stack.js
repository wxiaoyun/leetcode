// https://leetcode.com/problems/min-stack/

var MinStack = function() {
  this.stack = [];
  this.minAccum = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
  this.minAccum.push(Math.min(this.minAccum.at(-1) ?? Number.MAX_VALUE, val));
  this.stack.push(val);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  this.stack.pop();
  this.minAccum.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.stack.at(-1);
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  return this.minAccum.at(-1);
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
