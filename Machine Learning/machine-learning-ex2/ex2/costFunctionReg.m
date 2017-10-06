function [J, grad] = costFunctionReg(theta, X, y, lambda);
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
input_plugged_in = sigmoid(X * theta);
logged_version = log(input_plugged_in);
right_term = (y'*logged_version);
left_term = (log(1-input_plugged_in))'*(1 - y);
J =[ (-1/m) * [right_term' + left_term']];

sum = 0;
for i = 2:size(theta)
    sum = sum + theta(i)^2;
end
J = J + [(lambda/(2*m) * sum)];
%calculating the gradient
theta(1) = 0;
grad = [(1/m) * (X' * (input_plugged_in - y))] + [(lambda/m) * theta];





% =============================================================

end