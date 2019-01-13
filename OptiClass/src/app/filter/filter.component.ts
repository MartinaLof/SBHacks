import { Component, OnInit } from '@angular/core';
import { ExtracurricularComponent } from '../extracurricular/extracurricular.component';
import { MatDialog } from '@angular/material';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.css']
})
export class FilterComponent implements OnInit {

  modelFrom = 0;
  modelTo = 0;
  // newColor = false;
  mon = false;
  tue = false;
  wed = false;
  thu = false;
  fri = false;
  // id = document.getElementById('id');

  constructor(private dialog: MatDialog) { }

  // Button Toggle Colors
  monColor() {
    this.mon = !this.mon;
  }

  tueColor() {
    this.tue = !this.tue;
  }

  wedColor() {
    this.wed = !this.wed;
  }

  thuColor() {
    this.thu = !this.thu;
  }

  friColor() {
    this.fri = !this.fri;
  }

  formatLabel (value: number | null) {
    if (!value) {
      return 0;
    }
    if (value >= 1) {
      return '8:00 am';
    }
    return value;
  }

  /* Create a Form for adding athletes */
  onAddCurricular() {
    this.dialog.open(ExtracurricularComponent);
  }

  ngOnInit() {
  }

}
