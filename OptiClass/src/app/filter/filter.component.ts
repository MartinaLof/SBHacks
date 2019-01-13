import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.css']
})
export class FilterComponent implements OnInit {

  modelFrom = 0;
  modelTo = 0;

  constructor() { }

  formatLabel (value: number | null) {
    if (!value) {
      return 0;
    }
    if (value >= 1) {
      return '8:00 am';
    }
    return value;
  }

  ngOnInit() {
  }

}
