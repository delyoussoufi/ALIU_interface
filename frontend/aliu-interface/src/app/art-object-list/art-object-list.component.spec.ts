import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtObjectListComponent } from './art-object-list.component';

describe('ArtObjectListComponent', () => {
  let component: ArtObjectListComponent;
  let fixture: ComponentFixture<ArtObjectListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArtObjectListComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArtObjectListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
