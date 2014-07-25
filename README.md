
We want to deploy files without our users need to type a password, but we do not wont the files to be public, at the same time we want to know who is downloading files, how many times, from where ....
And we want to disable downloading a file user by user or with an expiry date.


###THE PLAN

 * Upload the files to a hidden  folder
 * With the application create for every user / file we want to share a symbolic link to the hidden folder.
 * Share with apache the folder with the simbolic links
 * send by email to every user their bespoke link














