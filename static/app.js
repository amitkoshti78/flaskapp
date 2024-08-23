var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $http) {
    $scope.formData = {};
    $scope.responseText = ""; // Holds the response text from Flask

    $scope.submitForm = function() {
        $http.post('/submit', $scope.formData)
        .then(function(response) {
            // Update responseText with the server's response
            $scope.responseText = response.data.message || "No response message";
            console.log("Server Response:", response.data);
        }, function(error) {
            // Handle error response
            $scope.responseText = "Error submitting form!";
            console.error("Submission Error:", error);
        });
    };
});
