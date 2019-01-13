import { Component, OnInit } from '@angular/core';
import { ExCurricularService } from 'src/app/shared/ex-curricular.service';
import { MatDialogRef } from '@angular/material';

@Component({
  selector: 'app-ex-curricular',
  templateUrl: './ex-curricular.component.html',
  styleUrls: ['./ex-curricular.component.css']
})
export class ExCurricularComponent implements OnInit {

  constructor(private service: ExCurricularService,
    public dialogRef: MatDialogRef<ExCurricularComponent>) { }

  ngOnInit() {
  }

  onClose() {
    this.service.form.reset();
    this.service.initializeFormGroup();
    this.dialogRef.close();
  }

}
