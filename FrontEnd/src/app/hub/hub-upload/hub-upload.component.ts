import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-hub-upload',
  templateUrl: './hub-upload.component.html',
  styleUrls: ['./hub-upload.component.css']

})
export class HubUploadComponent {

  fileData = null;

  constructor(private http: HttpClient) { }

  ngOnInit() {
  }

  onSubmit() {
    const formData = new FormData();
    formData.append('file', this.fileData);
    this.http.post('https://my-json-server.typicode.com/typicode/demo/posts', formData)
    .subscribe(res => {
        console.log(res);
        alert('Your Project was submitted successfully!');
      })
  }

}
