import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  courses = [
    { value: 'CMPSC4', viewValue: 'CMPSC 4'},
    { value: 'CMPSC8', viewValue: 'CMPSC 8'},
    { value: 'CMPSC12', viewValue: 'CMPSC 12'},
    { value: 'CMPSC18', viewValue: 'CMPSC 18'},
    { value: 'CMPSC28', viewValue: 'CMPSC 28'},
    { value: 'CMPSC32', viewValue: 'CMPSC 32'},
  ];

  constructor() { }

  ngOnInit() {
  }

}
