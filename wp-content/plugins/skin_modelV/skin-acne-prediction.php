<?php
/*
Plugin Name: Skin Acne Prediction
Description: A plugin to upload an image and predict acne conditions using a machine learning model.
Version: 1.0
Author: Your Name
*/

// Shortcode to display the form
function sap_prediction_form() {
    return '
        <div style="text-align: center; max-width: 600px; margin: 0 auto;">
            <h2>Analyze</h2>
            <form id="sapForm" enctype="multipart/form-data">
                <label for="sapImage">Please upload an image of the acne-affected area:</label>
                <br>
                <input type="file" id="sapImage" name="sapImage" accept="image/*" required>
                <button type="submit">Predict</button>
            </form>
            <br>
            <img id="uploadedImage" style="display:none; width: 100%; max-width: 400px; margin-top: 20px;"/>
            <p id="analyzingMessage"></p>
            <p id="result"></p>
        </div>
        <script src="' . plugin_dir_url(__FILE__) . 'sap-script.js"></script>
    ';
}
add_shortcode('sap_form', 'sap_prediction_form');
?>
