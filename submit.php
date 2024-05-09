<?php
  // Get the form data
  $name = $_POST['name'];
  $email = $_POST['email'];
  $whatsapp = $_POST['number']
  $topic = $_POST['topic']
  $message = $_POST['message'];

  // Send the email
  $to = 'domaingold7@gmail.com';
  $subject = 'Form Submission';
  $body = "Name: $name\nEmail: $email\nNumber: $whatsapp\nTopic: $topic\nMessage: $message";
  mail($to, $subject, $body);

  // Redirect back to the form page
  header('Location: index.html');
?>