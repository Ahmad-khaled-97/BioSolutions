import { Component, Injectable } from '@angular/core';
import {  HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

@Component ({
  selector: 'app-post-problem' ,
  templateUrl: './post-problem.component.html' ,
  styleUrls: ['./post-problem.component.css']
})

export class PostProblemComponent {
  title = '';
  tag = '';
  problemdef = '';
  titletext = '';
  tagtext = '';
  problemdeftext = '';
  json: [] ;
tools:[];
keys:any;
  uri = 'http://localhost:4200/';

  constructor(private http: HttpClient) { }

  postProblem(prbtitle, prbtag, prbdef) {
    const prb = {
      title : prbtitle,
     tagtext : prbtag,
     defination: prbdef
    };

    this.http.post(`http://localhost:5000/api/problem/submitProblem`, prb).subscribe((res: any) => {

      //this.json = (JSON.parse(res))['Sequence Alignemnt'][0];
      //console.log(JSON.parse(res));

     this.json = JSON.parse(res);
     console.log(this.json);
     this.keys = Object.keys(this.json);
     console.log(this.keys);
     this.tools = this.json;
    } );

  }}
  // students: Student[] = [];

  // constructor(private studentservice: StudentService) {}

  // ngOnInit() {
  //     const studentsObservable = this.studentservice.getStudents();
  //     studentsObservable.subscribe((studentsData: Student[]) => {
  //         this.students = studentsData;
  //     });
  // }




