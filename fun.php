
<?php
$txt_file=fopen('file.txt','r');
$a=1;
$line=fgets($txt_file);
$to_email =$line; 
$subject = "Loan Applied In AGH Loans";
$body = "Dear Customer , Your Application for loan has been received. Please wait till your Loan gets Approved. Thanking you , Reagrds AGH Team";
$headers = "From: aghloansandservices@gmail.com";
if(mail($to_email, $subject, $body, $headers)) 
{ 
echo "Email successfully sent to $to_email...";
fclose($txt_file);
} 
else {

echo "Email sending failed...";

} 

?>
