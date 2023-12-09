import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtObjectDetailComponent } from './art-object-detail.component';

describe('ArtObjectDetailComponent', () => {
  let component: ArtObjectDetailComponent;
  let fixture: ComponentFixture<ArtObjectDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArtObjectDetailComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArtObjectDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
